##TODO: custom script to clone repos from projects.yaml
clone: # Clone all repos 
	cd ../server
	git clone https://github.com/yaderson/api-server.git || git pull
##TODO: custom script to run make from projects.yaml
up: # Run all projects
	cd ../server/api-server
	ls
	make run
##TODO: custom script to down make from projects.yaml
down: # Down all projects
	cd ../server/api-server
	make down