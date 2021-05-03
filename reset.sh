ARGS=$(cat jvmArgs.txt)
# Remove world files
rm -rf world*
echo "World Deleted"
# Edit seed in server.properties
python ./updateProperties.py $1
echo "Loaded Seed " $1
# Start server
java $ARGS -jar server.jar nogui .