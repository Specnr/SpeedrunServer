ARGS=$(cat jvmArgs.txt)

# Edit seed in server.properties
python3 ./updateProperties.py $1
[ $# -gt 0 ] && echo "Loaded Seed " $1
rm -rf world*
# Start server
java $ARGS -jar fabric-server-launch.jar nogui .