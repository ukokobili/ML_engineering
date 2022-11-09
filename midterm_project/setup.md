bentoml serve insurance.py:svc

bentoml serve insurance.py:svc --reload

bentoml models list 

bentoml models get tag_name

bentoml serve --production

# deployment
bentoml build

bentoml containerize

aws elastic container registry - store the code
    create
        name
    view push command
    copy and paste login details
    get tag from the built tag image - bentoml containerize
    push the image to ECR - copy and paste link

asw elastic container service - to run a container
    cluster 
        network only
            cluster name
                create
                view
    task - a unit that helps scale service
        fargate
            task name
            os:linux
            task:0.5
            task cpu:0.25
                add container
                    name
                    image - copy URI from ECR and paste
                    soft limit: 256
                    port mapping: 3000
                    add
                create
                ...task
    cluster 
        link on cluster created
        tasks
            run new task
                fargate
                os:linux
                cluster VPC: select default
                subnet: region
                security group: 
                    inbound rules for security group
                        custom tcp 3000
                        save
                create
            refresh
            inter the task 
            copy public ip and paste url - ip:3000

bentoml export --help: push bentoml to a local or remote destination.
how to integrate s3 into streamlit                                         


