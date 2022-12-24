echo "\nDeploying Ghost...\n"

ansible-playbook deploy-ghost.yml -i inventory/gcp.yml