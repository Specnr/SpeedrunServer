ARGS=$(cat jvmArgs.txt)
echo "Generating seed..."
seed=$(python3 findSeed.py)
echo "Seed Found"

# Edit seed in server.properties
python3 ./updateProperties.py $seed
rm -rf world*
# Start server
java $ARGS -jar fabric-server-launch.jar nogui .