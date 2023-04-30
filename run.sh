#!/bin/bash


case "$1" in
    "docker_build")
        echo "Building docker"
        docker-compose build
        ;;
    "docker_up")
        echo "Starting docker"
        docker-compose up
        ;;
    "docker_down")
        echo "Stopping docker"
        docker-compose down
        ;;
    "docker_restart")
        echo "Restarting docker"
        docker-compose restart
        ;;
    "make_migrations")
        echo "Making migrations"
        docker-compose exec web python manage.py makemigrations
        ;;
    "migrate")
        echo "Migrating"
        docker-compose exec web python manage.py migrate
        ;;
    "create_superuser")
        echo "Creating superuser"
        docker-compose exec web python manage.py createsuperuser
        ;;
    "run_tests")
        echo "Running tests"
        docker-compose exec web python manage.py test
        ;;
    "collect_static")
        echo "Collecting static"
        docker-compose exec web python manage.py collectstatic
        ;;
    "runserver")
        echo "Running server"
        docker-compose exec web python manage.py runserver
        ;;
    "shell")
        echo "Running shell"
        docker-compose exec web python manage.py shell_plus
        ;;
    "startapp")
        echo "Starting app"
        docker-compose exec web python manage.py startapp $2
        ;;
    *)
        echo "Invalid command"
        exit 1
        ;;
esac

