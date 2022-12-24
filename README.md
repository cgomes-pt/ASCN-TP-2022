# ASCN TP 2022

- Criar cluster
`chmod +x create.sh && ./create.sh`

- Dar deploy de ghost 
`chmod +x deploy.sh && ./deploy.sh`

- Destruir cluster
`chmod +x destroy.sh && ./destroy.sh`



## Exemplo de um ficheiro secret.yml
```
apiVersion: v1
kind: Secret
metadata:
	name: ghost-data
type: Opaque
data:
	password: UGFzc3dvcmQkMTIzNDU2  # Password$123456
	root_password: UGFzc3dvcmQkMTIzNDU2  # Password$123456
```

## Ver erros
- Ver o nome do pod
`kubectl get pods`
- Ver qual é o problema
`kubectl logs <nome_do_pod>`
