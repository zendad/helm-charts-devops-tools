# ansible-awx

[ansible-awx](https://github.com/ansible/awx) is an opensource implementation of the [ansible tower](https://www.ansible.com/products/tower).


### Prerequisites
When installing AWX you have the option of building your own images or using the images provided on DockerHub (see [awx_web](https://hub.docker.com/r/ansible/awx_web/) and [awx_task](https://hub.docker.com/r/ansible/awx_task/))

A Kubernetes deployment will require you to have access to a Kubernetes cluster as well as the following tools:

- [helm](https://docs.helm.sh/using_helm/#quickstart-guide)


The default resource requests per-pod requires:

> Memory: 6GB
> CPU: 3 cores

