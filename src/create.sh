echo "\nCreating cluster...\n"

ansible-playbook create-gke-cluster.yml -i inventory/gcp.yml