from errbot import BotPlugin, botcmd, re_botcmd
import re
from kubernetes import config,client

class Kube(BotPlugin):
  @botcmd
  def context_list(self, msg, args):
      """
      List all contexts in the kubeconfig file.
      """
      yield("Context in the Kubeconfig:")
      for context_name in self.list_context():
          yield(context_name)
          
  def list_context(self):
      (context_list, context_current) = config.list_kube_config_contexts("/errbot/kubeconfig")
      result = []
      for context in context_list:
          result.append(context["name"])
      return result

  @botcmd(split_args_with=None)
  def cluster_health(self, msg, args):
      """Simpler checker nodes, pods and workload controllers.
      """
      if len(args) != 1:
          yield("This command need context name as the only parameter.")
          yield("Here is the context list:")
          for context_name in self.list_context():
              yield(context_name)
          return

      context_name = args[0]
      api_instance = self.get_instance(context_name)
      node_list = api_instance.list_node()
      # Node
      yield("Checking Nodes...")
      for node in node_list.items:
          name = node.metadata.name
          status = "NotReady"
          last_condition = node.status.conditions[-1:][0]
          if (last_condition.type == "Ready" and
                  last_condition.status == "True"):
              status = "Ready"
          if status != "NoReady":
              yield("{} {}\n".format(name, status))

  def get_instance(self,context_name, api_version="core_v1"):
      api_client = config.load_kube_config(
          config_file="/errbot/kubeconfig",
          context=context_name)
      api_instance = client.CoreV1Api(api_client)
      return api_instance
      
  # https://www.kancloud.cn/smilesb101/python3_x/296108
  @botcmd(split_args_with=None)
  def fib(self, msg, args):
    n, a, b = 0, 0, 1
    while n < int(args[0]):
      yield(b)
      a, b = b, a + b
      n = n + 1
    return 'done'