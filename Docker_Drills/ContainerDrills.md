1. **Run the `nginx` image in detached mode.**
    - Map port 8080 on the host to port 80 in the container.

```bash
docker run --name mynginx -p 8080:80 -d -v ~/Public/webPage:/usr/share/nginx/html nginx:1.29
```

-d → for detached mode, it’ll run in background.

—name → to give a name to container(good practice) as random name is taken if not given.

-v → to mount the volume in which your html file exists to the nginx serving directory which is /usr/share/nginx/html 

-p → to map ports from my pc port to docker container port

⇒ always define the version while running a container

- Verify that `nginx` is serving correctly from the container.

```bash
docker logs mynginx(or containerID)
```

- Find the container’s IP and confirm whether it can be accessed using `curl` from the host.

```bash
docker ps # to see the containerID
docker inspect containerID 
# use grep to specifically get IPAddress
docker inspect containerID | grep "IPAddress"
curl ipaddress:8080
```

- Identify the port mappings and process ID associated with the container.

```bash
docker ps # for containerID
docker port containerID # for port mappings
docker inspect containerID | grep -i "pid" 
ps -p pidofcontainer #check in host also 
```

1. **Run the `ubuntu` image in interactive mode.**
- Start a container with a shell session.

```bash
docker run --rm --name myUbuntu -it --label owner=anant_ubuntu ubuntu:22.04
# for already created container
docker start -ai anant_ubuntu
```

- List all processes running inside the container.

```bash
docker exec -it alpine_anant ps
```

- Inspect the container's file system layout.

```bash
explore in there
```

- Determine the container's PID namespace on the host and compare it with host processes.

```bash
docker inspect anant_ubuntu | grep -i "PID"
ps -p 87331 # acting as a bash in the host system
ls -l /proc/1/ns/pid # host pid namespace(init process)
ls -l /proc/PIDOFCONTAINER/ns/pid # completely differenct namespace
# show the process id in the container also
docker exec -it anant_ubuntu ps aux
```

1. **List and inspect running and stopped containers.**
    - Run two different containers and stop one of them.
    
    ```bash
    do it yourself, this you must know
    ```
    
    - List all containers (not just running ones) and record key info: container ID, image, command, status.
    
    ```bash
    docker ps -a
    ```
    
    - Use system tools to find out which network and storage namespaces are in use.
        
        ```bash
        #same steps as getting PID namespace
        ls -l /proc/PIDOFCONTAINER/ns/net
        
        # for storage
        ls -l /proc/PID/ns/mnt
        ```
        
2. **Inspect container metadata.**
    - Use Docker CLI tools to inspect a running container.
    - Find and note:
        - The internal container IP(Done)
        - Host directory that stores container files
            
            ```bash
            docker inspect bfac45a75eb4 | grep -i "host"
            ```
            
        - How environment variables are passed in
            
            ```bash
            docker run -it --name alpine_environment_var -e VAR1=2 alpine:3.22
            echo $VAR1 #run in container
            
            #also can pass .env file
            docker run -it --name alpine_env_file --env-file .env alpine:3.22
            ```
            
    - Determine where logs and layer data are stored on disk.
        
        ```bash
        #logs
        cat ~/../../var/lib/docker/containers/<container id>/<container id>-json.log
        #data
        docker inspect contID | grep -i "data"
        ls -l ~/../../var/lib/docker/overlay2/<container id>/diff
        ```
        
3. **Capture and view logs.**
    - Run a container using the `busybox` image to generate output in a loop.
        
        ```bash
        docker run -it --name myBusyBox busybox:1.37 sh -c 'while true; do echo "Hello bhaiyaa.."; sleep 1; done'
        ```
        
    - Observe how the logs appear in real time.
        
        ```bash
        docker logs -f containerID # f(follow) real-time output
        ```
        
    - Stop the container and verify whether you can still view its logs. (yes it works, can see previous logs)
    - Identify where logs are stored and who owns them on the host system.
        
        ```bash
        /var/lib/docker/containers/<container id>/<container id>-json.log
        # for ownership do
        ls -l /var.... # we see root:root  (so root user and root group) HOST's root owns it,
        # for security because docker daemon controls it
        ```
        
4. **Exec into a running container.**
    - Start a `python` container in the background.
        
        ```bash
        docker run -dit --name my-python python:3.10-slim
        ```
        
    - Enter the container's shell session.
        
        ```bash
        docker start my-python
        docker exec -it my-python sh
        
        # otherwise you could do "docker run -it --name my-python python:3.10-slim sh"
        # to directly get into the shell while creating
        
        # also with docker start -ai my-python , we land up in the python shell
        # because default container is python,so it attaches it, that's why we 
        # first started then exec into the shell
        
        ```
        
    - Create a temporary file or install a package inside the container.(Do normally)
    - Exit and restart the container — check if your changes persist.(Yes)
5. **Pause, stop, restart, and remove containers.**
    - Practice pausing and unpausing a container and monitor its effect on processes.
        
        ```bash
        docker start myBusyBox #continously printing Hello container
        docker logs -f myBusyBox # we can see Hello printing
        docker pause myBusyBox
        
        docker logs -f myBusyBox # we can see Hello no more executing
        docker unpause myBusyBox 
        ```
        
    - Stop and remove containers cleanly.
        
        ```bash
        docker stop {containerName}
        docker rm {containerName}
        
        # for bulk stopped container cleanup
        docker container prune
        ```
        
    - Examine what remains in the system after removal (e.g., volumes, networks).
        
        ```bash
        docker inspect containeID
        # got /var/run/docker/netns/something... and var/lib/docker/overlay2/.../diff
        # both are (non persistent, removed on container removal)
        
        # until now i had no volumes, i only wrote data in container's writable layer(/overlay2)
        # user created volumes are persisted in the `/var/lib/docker/volumes/
        
        # user created networks, volumes are persisted(not removed)
        ```
        
        ```bash
        # for persistent storage we need to create like
        docker volume create alpine_volume
        docker run -it -v alpine_volume:/app --name alpine_anant alpine:3.22
        # now create coding.py in /app folder in container,
        # then go to /var/lib/docker/volumes/alpine_volume/_data you'll see coding.py there
        docker rm alpine_anant
        # still you'll have your files
        # use docker volume prune to remove all volumes not attached to any container
        ```
        
    - Compare disk usage before and after cleanup operations.
        
        ```bash
        docker system df
        docker volume rm alpine_volume
        docker system df
        ```