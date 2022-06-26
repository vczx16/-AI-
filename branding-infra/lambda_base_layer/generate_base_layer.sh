#generates a base layer for the lambda function
docker rm layer-container
#remove the container first

#build the base layer
docker build -t base-layer

#rename it to layer-container
docker run --name layer-container base layer

docker cp layer-container:layer.zip . && echo "created layer.zip with updated base  layer "