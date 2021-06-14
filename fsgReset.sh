ARGS=$(cat jvmArgs.txt)
echo "Generating seed..."
seed=$(python3 findSeed.py)
echo "Seed Found"
# Edit seed in server.properties
python3 ./updateProperties.py $seed

# Start server
java $ARGS -jar server.jar nogui .