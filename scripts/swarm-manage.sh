#!/bin/bash

# Docker Swarm Management Script for App Labs API

set -e

STACK_NAME="app-labs"
SERVICE_NAME="app-labs"

case "$1" in
    "deploy")
        echo "🚀 Deploying to Docker Swarm..."
        docker stack deploy -c docker-stack.yml $STACK_NAME
        echo "✅ Deployment initiated!"
        ;;
    "update")
        echo "🔄 Updating service..."
        docker service update --force ${STACK_NAME}_${SERVICE_NAME}
        echo "✅ Service update initiated!"
        ;;
    "logs")
        echo "📋 Service logs:"
        docker service logs ${STACK_NAME}_${SERVICE_NAME}
        ;;
    "status")
        echo "📊 Service status:"
        docker service ls --filter "name=${STACK_NAME}_${SERVICE_NAME}"
        docker service ps ${STACK_NAME}_${SERVICE_NAME}
        ;;
    "remove")
        echo "🗑️ Removing stack..."
        docker stack rm $STACK_NAME
        echo "✅ Stack removed!"
        ;;
    "health")
        echo "🏥 Health check:"
        if curl -f http://localhost:4000/health > /dev/null 2>&1; then
            echo "✅ Service is healthy!"
        else
            echo "❌ Service is not responding!"
        fi
        ;;
    *)
        echo "Usage: $0 {deploy|update|logs|status|remove|health}"
        echo ""
        echo "Commands:"
        echo "  deploy  - Deploy the stack to Docker Swarm"
        echo "  update  - Force update the service"
        echo "  logs    - Show service logs"
        echo "  status  - Show service status"
        echo "  remove  - Remove the stack"
        echo "  health  - Check service health"
        exit 1
        ;;
esac 