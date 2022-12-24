echo "\nDestroying cluster...\n"

ansible-playbook destroy-gke-cluster.yml -i inventory/gcp.yml