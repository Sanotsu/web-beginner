<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [k8s 常用基础命令](#k8s-%E5%B8%B8%E7%94%A8%E5%9F%BA%E7%A1%80%E5%91%BD%E4%BB%A4)
- [k8s 从节点加入集群](#k8s-%E4%BB%8E%E8%8A%82%E7%82%B9%E5%8A%A0%E5%85%A5%E9%9B%86%E7%BE%A4)
- [移除节点（主节点执行）](#%E7%A7%BB%E9%99%A4%E8%8A%82%E7%82%B9%E4%B8%BB%E8%8A%82%E7%82%B9%E6%89%A7%E8%A1%8C)
- [查看指定 pod 描述](#%E6%9F%A5%E7%9C%8B%E6%8C%87%E5%AE%9A-pod-%E6%8F%8F%E8%BF%B0)
- [helm 安裝卸载项目](#helm-%E5%AE%89%E8%A3%9D%E5%8D%B8%E8%BD%BD%E9%A1%B9%E7%9B%AE)
- [安裝 kafka gui kfdrop](#%E5%AE%89%E8%A3%9D-kafka-gui-kfdrop)
- [k8s 中的 kafka 订阅消费测试](#k8s-%E4%B8%AD%E7%9A%84-kafka-%E8%AE%A2%E9%98%85%E6%B6%88%E8%B4%B9%E6%B5%8B%E8%AF%95)
- [k8s 安裝 emqx](#k8s-%E5%AE%89%E8%A3%9D-emqx)
- [切换 emqx 显示日志级别](#%E5%88%87%E6%8D%A2-emqx-%E6%98%BE%E7%A4%BA%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB)
- [k8s 安裝 elastic](#k8s-%E5%AE%89%E8%A3%9D-elastic)
- [ubuntu 修改环境变量](#ubuntu-%E4%BF%AE%E6%94%B9%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
- [containerd 部分命令](#containerd-%E9%83%A8%E5%88%86%E5%91%BD%E4%BB%A4)
- [解压文件夹](#%E8%A7%A3%E5%8E%8B%E6%96%87%E4%BB%B6%E5%A4%B9)
- [修改主机名](#%E4%BF%AE%E6%94%B9%E4%B8%BB%E6%9C%BA%E5%90%8D)
- [ubuntu 设置固定 ip](#ubuntu-%E8%AE%BE%E7%BD%AE%E5%9B%BA%E5%AE%9A-ip)
- [使用 nerdctl 访问指定 k8s 容器 bash](#%E4%BD%BF%E7%94%A8-nerdctl-%E8%AE%BF%E9%97%AE%E6%8C%87%E5%AE%9A-k8s-%E5%AE%B9%E5%99%A8-bash)
- [nginx 重新加载配置](#nginx-%E9%87%8D%E6%96%B0%E5%8A%A0%E8%BD%BD%E9%85%8D%E7%BD%AE)
- [测试机配置好 k8s local 地址后无法访问的问题](#%E6%B5%8B%E8%AF%95%E6%9C%BA%E9%85%8D%E7%BD%AE%E5%A5%BD-k8s-local-%E5%9C%B0%E5%9D%80%E5%90%8E%E6%97%A0%E6%B3%95%E8%AE%BF%E9%97%AE%E7%9A%84%E9%97%AE%E9%A2%98)
- [server 节点重启后删除 pv 失败的错误](#server-%E8%8A%82%E7%82%B9%E9%87%8D%E5%90%AF%E5%90%8E%E5%88%A0%E9%99%A4-pv-%E5%A4%B1%E8%B4%A5%E7%9A%84%E9%94%99%E8%AF%AF)
- [使用 br 备份 tidb 数据](#%E4%BD%BF%E7%94%A8-br-%E5%A4%87%E4%BB%BD-tidb-%E6%95%B0%E6%8D%AE)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

- kubectl
  - Kubernetes 命令行工具，使得你可以对 Kubernetes 集群运行命令。 你可以使用 kubectl 来部署应用、监测和管理集群资源以及查看日志。
- kubeadm
  - 使用 kubeadm 工具来创建和管理 Kubernetes 集群。 该工具能够执行必要的动作并用一种用户友好的方式启动一个可用的、安全的集群。

### k8s 常用基础命令

查看节点状态:

```sh
kubectl get nodes -A --output=wide
kubectl get pod -A
kubectl get replicasets -A
```

安裝插件(例如flannel):

```sh
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# 都是yaml配置，都形如
# kubectl apply -f <tool-config>.yaml
```

查看指定命名空间 -n(容器 -c)下指定 pod 的日志:

```sh
kubectl logs -f  kube-proxy-4wnk5 -n kube-system
```

追踪名称空间 nsA 下容器组 pod1 中容器 container1 的日志:

```sh
kubectl logs -f pod1 -c container1 -n nsA
```

kube 配置导入环境变量（就是登錄的 token 信息）

```sh
export KUBECONFIG=/etc/kubernetes/admin.conf
```

重裝 master(master 节点初始化)

```sh
kubeadm reset
```

清除旧配置

```sh
rm -rf /etc/cni/
ifconfig cni0 down
ifconfig flannel.1 down
ip link delete cni0
ip link delete flannel.1
iptables-save | awk '/^[*]/ { print $1 }
                     /^:[A-Z]+ [^-]/ { print $1 " ACCEPT" ; }
                     /COMMIT/ { print $0; }' | iptables-restore
ipvsadm -C
```

修改配置，重新安裝(示例):

```sh
# 安装 Kubernetes 控制平面
kubeadm init --config init-config.yaml
kubectl taint nodes --all node-role.kubernetes.io/master-
# 安裝网络插件
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
# 檢查节点状态（網絡插件未装好，节点notready，后面的大部分操作都做不了）
kubectl get nodes -A --output=wide
# 查看kube-flannel-ds-XXX是否在running，如果是，但node还是notready，重啟该node主機 reboot
kubectl get pod -A
# 安装nfs provisioner
helm install --create-namespace -n persistent-storage nfs-subdir-external-provisioner \
nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
--set nfs.server=192.168.137.84,nfs.path=/kubernetes,storageClass.name=managed-nfs-storage,storageClass.defaultClass=true,storageClass.accessModes=ReadWriteManybash
# 安裝kubesphere
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.2.1/kubesphere-installer.yaml
kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.2.1/cluster-configuration.yaml
# 查看kubesphere安裝進度
kubectl logs -n kubesphere-system $(kubectl get pod -n kubesphere-system -l app=ks-install -o jsonpath='{.items[0].metadata.name}') -f
```

### k8s 从节点加入集群

```sh
### （主节点）
# 創建 token：
kubeadm token create
# 查看 token：
kubeadm token list
# 生成 token hash：
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.\* //'

### （从节点）
# 加入集群：
kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash> --cri-socket /run/containerd/containerd.sock

# 示例:
kubeadm join 192.168.137.84:6443 --token zode2g.7v61wgq4885fml1x --discovery-token-ca-cert-hash sha256:7b01da2a5e21383a25a1e5813d60de11fa554bc7f33e06f1efe8555754240b0f --cri-socket /run/containerd/containerd.sock
```

### 移除节点（主节点执行）

```sh
# 清空指定节点
kubectl drain <node name>
# 清空没有报错，再删除该节点
kubectl delete node <node name>
# (从节点执行join失败后，执行reset)
kubeadm reset   #该命令尽力还原由 kubeadm init 或 kubeadm join 所做的更改
```

### 查看指定 pod 描述

```sh
kubectl describe pod nfs-subdir-external-provisioner-76cb884b7c-5msdg -n default
kubectl describe pod ks-apiserver-7d8d4c8ccf-9665z -n kubesphere-system
kubectl rollout restart statefulsets -n minio
```

### helm 安裝卸载项目

```sh
# 卸载指定命名空间指定项目：
helm uninstall kafka --namespace kafka
# 强制删除指定命名空间下指定 pod：
kubectl delete pod kafka-1 --grace-period=0 --force --namespace kafka
# 指定配置文件安裝项目
helm install kafka bitnami/kafka --version 12.10.0 --namespace kafka -f /home/flos/bitnami-kafka-config.yaml
```

### 安裝 kafka gui kfdrop

```sh
# 先用 git 下载对应仓库：
git clone https://github.com/obsidiandynamics/kafdrop && cd kafdrop
# 进入该文件夹下后，終端执行安裝命令：
helm upgrade -i kafdrop chart --namespace kafka --set image.tag=3.29.0 --set kafka.brokerConnect=kafka-headless.kafka.svc.cluster.local:9092 --set server.servlet.contextPath="/" --set cmdArgs="--message.format=AVRO --schemaregistry.connect=http://localhost:8080" --set jvm.opts="-Xms32M -Xmx64M"
```

### k8s 中的 kafka 订阅消费测试

```sh
# kafka 生产者测试：
kafka-console-producer.sh --broker-list kafka-0.kafka-headless.kafka.svc.cluster.local:9092,kafka-1.kafka-headless.kafka.svc.cluster.local:9092,kafka-2.kafka-headless.kafka.svc.cluster.local:9092 --topic MessageLv4
# kafka 消费者测试：
kafka-console-consumer.sh --bootstrap-server kafka-0.kafka-headless.kafka.svc.cluster.local:9092,kafka-1.kafka-headless.kafka.svc.cluster.local:9092,kafka-2.kafka-headless.kafka.svc.cluster.local:9092 --topic MessageLv4
```

### k8s 安裝 emqx

```sh
# 创建对应命名空间
kubectl create namespace emqx
# 配置对应configmap
kubectl create configmap emqx-base-config --from-file=/home/flos/some-config-files/emqx.conf -n emqx
kubectl create configmap emqx-kafka-config --from-file=/home/flos/some-config-files/emqx_kafka.conf -n emqx
kubectl create configmap emqx-loaded-plugins --from-file=/home/flos/some-config-files/loaded_plugins -n emqx
# 根据配置文件进行安裝
kubectl apply -f /home/flos/some-config-files/emqx.yaml
# 卸载emqx
kubectl delete -f /home/flos/some-config-files/emqx.yaml
```

### 切换 emqx 显示日志级别

进入 emqx 容器，在其终端打命令：

```
emqx_ctl log set-level debug
```

默认用的 warn 级别，切到 debug 可以看到连接过程

### k8s 安裝 elastic

```sh
## 安装eck operator
## https://download.elastic.co/downloads/eck/2.0.0/crds.yaml
## https://download.elastic.co/downloads/eck/2.0.0/operator.yaml
# 如果能联网访问可以直接执行：
kubectl create -f https://download.elastic.co/downloads/eck/2.0.0/crds.yaml
# 不能访问这先下载下來：
kubectl create -f crds.yaml
kubectl apply -f operator.yaml

## 安装 Elastic、Kibana
kubectl apply -f /home/flos/some-config-files/elastic.yaml
kubectl apply -f /home/flos/some-config-files/fluentd-es-configmap.yaml
kubectl apply -f /home/flos/some-config-files/fluentd-es-ds.yaml
```

### ubuntu 修改环境变量

用于所有用户

要使环境变量对所有用户有效，可以修改 profile 文件：

```sh
sudo vim /etc/profile
```

添加语句：

```sh
export CLASS_PATH=./JAVA_HOME/lib:$JAVA_HOME/jre/lib
export KUBECONFIG=/etc/kubernetes/admin.conf
```

注销或者重启可以使修改生效，如果要使添加的环境变量马上生效：

```sh
source /etc/profile
```

### containerd 部分命令

```sh
# 查看指定命名空间下的鏡像列表：
ctr -n <namespace> i list
eg:
ctr -n k8s.io i list |grep 'jdk'
# 刪除指定命名空间下指定镜像：
ctr -n k8s.io i rm <image-name>

# crictl 是 kubernetes cri-tools 的一部分，是专门为 kubernetes 使用 containerd 而专门制作的，提供了 Pod、容器和镜像等资源的管理命令。
# 可以理解为crictl 操作的时候指定了 containerd 的 namespace 为 k8s.io。
# --查看k8s命名空间的鏡像
crictl img list

# ctr 或者 nerdctl 中假如没有指定 -n k8s.io 则表示查看非 kubernetes 中的容器、镜像资源；
# ctr 或者 nerdctl 中指定了 -n k8s.io 则表示查看 kubernetes 中的容器、镜像资源。
```

### 解压文件夹

```sh
# 原始位置 到 目标位置
tar -xvf some-config-files/zentao-backup.tar /kubernetes/zentao-zentao-pvc-pvc-e9fcb070-bb66-4968-949c-dff5ad562fe9/tmp/
# tar解压tar.gz文件时报tar not found in archive解决办法:
# 用tar -zxvf  abc.tar.gz ./ab/解压文件的时候报tar not found in archive，只要加上-C参数就可以了(注意了是大写)
tar -zxvf  abc.tar.gz  -C ./ab/
```

### 修改主机名

修改 `/etc/hostname` 文件

### ubuntu 设置固定 ip

修改 `/etc/netplan/XXX.yaml`，一个示例:

```yaml
# Let NetworkManager manage all devices on this system
network:
  ethernets:
    enp0s9:
      dhcp4: true
    enp0s8:
      dhcp4: true
    ens33:
      dhcp4: no
      addresses:
        - 192.168.29.55/24
      gateway4: 192.168.29.254
      nameservers:
        addresses: [8.8.8.8, 114.114.114.114]
  version: 2
  renderer: networkd
```

### 使用 nerdctl 访问指定 k8s 容器 bash

```sh
nerdctl --namespace k8s.io exec -it -u root aaf7231fa664b /bin/bash
nerdctl pull 192.168.188.106:5000/i2dsp_emg_data:1.2.202111181410-dev
```

### nginx 重新加载配置

```sh
sudo nginx -s reload
# OR：
sudo systemctl reload nginx
# OR：
sudo service nginx reload

sudo service nginx start    # 启动
sudo service nginx stop     # 停止
sudo service nginx restart  # 重启
```

---

### 测试机配置好 k8s local 地址后无法访问的问题

可能是本地主机启用了 MDNS，关闭即可。

```sh
# 测试：wireshark抓包,过滤设置：
dns || mdns || ip.dst_host == 192.168.188.118
# 如果.local协议是MDNS那八九不离十了。

# 关闭mdns有做的操作：
sudo systemctl stop avahi-daemon.socket
sudo systemctl stop avahi-daemon.service
sudo systemctl disable --no-reload avahi-daemon.socket
sudo systemctl disable --no-reload avahi-daemon.service
systemctl mask avahi-daemon

# 修改文件 `/etc/systemd/resolved.conf`，添加：
MulticastDNS=no

# 最后再重启主机。

# ------------------

# 查看是否已关闭mdns：
sudo systemctl status avahi-daemon

# 查看k8s pod域名能不能解析到ip地址，类似：
nslookup minio-console.minio.svc.cluster.local

http://v2-i2dsp-emg-map-service.development.svc.cluster.local:10185

# 在配置网关供pod的local解析失败时，直接修改连接的网关无效，可以尝试卸载原本的network-manager：

sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
sudo unlink /etc/resolv.conf
echo nameserver 192.168.188.118 | sudo tee /etc/resolv.conf
sudo apt remove network-manager

# 卸载之后，要重启启动网卡，开启dhcp，命令类似：
ip a  # 找到网卡名称
ifconfig <网卡名> up  # 启动网卡
touch /etc/netplan/01-network-manager-all.yaml

# 写入类似内容： // 开启dhcp

# Let NetworkManager manage all devices on this system
network:
  ethernets:
    enp0s3:
      dhcp4: true
  version: 2
  renderer: networkd
```

---

### server 节点重启后删除 pv 失败的错误

server 节点重启后，syslog 中可能会有类似

```log
"There were many similar errors. Turn up verbosity to see them." err="orphaned pod \"1d848937-206d-4c39-9faf-76eb0900dae4\" found, but error not a directory occurred when trying to remove the volumes dir" numErrs=8
```

删除 pv 失败的错误。

如果没有手动删除对应的文件夹的话，服务是创建不起来的，所以需要找到对应的文件夹，清空。
以`1d848937-206d-4c39-9faf-76eb0900dae4`为例

```sh
cd /var/lib/kubelet/pods/1d848937-206d-4c39-9faf-76eb0900dae4/volumes
rm -rf *
```

然后刷新 syslog，解决下一个无法删除的问题，直到全部处理完（不删除前一个，看不到后一个）。

最好使用脚本，因为一般会有很多

---

### 使用 br 备份 tidb 数据

https://gitbook.curiouser.top/origin/tidb-br-backup-restore.html

查看单个环境变量: `echo $PATH`

查看所有环境变量: `env`

1 下载 tidb 的备份工具 br，并放置到 tidb 的 pd 节点中

下载 tidb-toolkit，https://download.pingcap.org/tidb-toolkit-v5.3.0-linux-amd64.tar.gz

2 设置需要导出到 minio 的帐号密码环境变量

```sh
export AWS_ACCESS_KEY_ID=i2dsp
export AWS_SECRET_ACCESS_KEY=8qbWHmZqKQtYU4et8g0u
```

3 使用 br 将 tidb 的数据备份到 MinIo（在 br 工具的文件夹下执行）

```sh
./br backup full \
    --pd "192.168.188.104:2379" \
    --storage "s3://backup-tidb/?endpoint=http://192.168.188.118:9000" \
    --ratelimit 128 \
    --log-file backupfull.log
```

备份到 pd 本机

```sh
./br backup full \
    --pd "192.168.188.104:2379" \
    --storage "local:///home/TIDBbak0726" \
    --ratelimit 128 \
    --log-file backupfull.log

```

---
