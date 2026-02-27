# Network Agent - OCP Deployment

## Files

- **Dockerfile** - Container image definition
- **ocp-deploy.yaml** - Single YAML file with all OCP resources (Deployment, Service, Route)

## Quick Deploy

### 1. Build & Push to Docker Hub

```bash
docker build -t network-agent:latest .

# Login to Docker Hub
docker login

# Tag and push
docker tag network-agent:latest <your-docker-hub-username>/network-agent:latest
docker push <your-docker-hub-username>/network-agent:latest
```

**Update ocp-deploy.yaml:** Replace `<your-docker-hub-username>` in the Deployment image field

### 2. Deploy to OCP

```bash
# Login to CRC
oc login -u kubeadmin -p <password> https://api.crc.testing:6443

# Deploy
oc apply -f ocp-deploy.yaml

# Check status
oc get pods
oc get route
```

### 3. Access

```bash
# Via route
curl http://network-agent.apps-crc.testing/getSiteDetails

# Or check route URL
oc get route network-agent
```

## Cleanup

```bash
oc delete -f ocp-deploy.yaml
```

