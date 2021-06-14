ARGS=$(cat jvmArgs.txt)
seed=$(python3 findSeed.py)
# Edit seed in server.properties
python3 ./updateProperties.py $seed

# Start server
java $ARGS -jar server.jar nogui .