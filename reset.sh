ARGS=$(cat jvmArgs.txt)
# Remove world files
rm -rf prev_world*
echo "World Deleted"
# Keep previous world for verification
mv world prev_world
echo "Backed up previous world"
# Edit seed in server.properties
python3 ./updateProperties.py $1
echo "Loaded Seed " $1
# Start server
java $ARGS -jar server.jar nogui .