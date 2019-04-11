
# 基于 Docker 的 Errbot 代码调试 

## Step1. 挂载代码启动容器
```bash
docker run -p 5678:5678 -v `pwd`/code:/errbot -ti errbot:alpine sh
/errbot # errbot
```

## Step2. 代码增加配置项

注意要在启动的 config.py 文件头增加如下的调试配置

```python
import ptvsd
ptvsd.enable_attach(address =('0.0.0.0',5678))
ptvsd.wait_for_attach()
```
## Step3. vscode 增加调试支持
对应的 vscode 调试配置如下：

```json
    {
      "name": "Errbot Debug",
      "type": "python",
      "request": "attach",
        "pathMappings": [
          {
            "localRoot": "${workspaceRoot}/errbot/code",
            "remoteRoot": "/errbot",
          }
        ],
        "port": 5678,
        "host":"127.0.0.1"
    }
```

注: 通过 slack 指令 `!restart` 重启 errbot 时，需要重新连接调试器..

## Kubernetes 节点状态调试

```bash
# 获取当前的上下文配置
!context list
# 获取当前集群的节点状态
!cluster health default

# fib 数列测试
!fib 10
```