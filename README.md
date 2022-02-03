## Test api

### Endpoints

    # DRF endpoint
    /
    
    # OpenApi endpoint
    /docs/
    # Redoc endpoint
    /redoc/

    # Schema endpoint
    /schema/
    
    # Admin panel
    /admin/

### Configure app

Add environment variables

    cp .env.template .env
    ln .env env/common.env

    cp env/back.env.template env/back.env
    cp env/db.env.template env/db.env

Enter in admin patel

    username: admin
    password: password

___

### Docker

    # Run app
    docker-compose up runserver

    # Run tests
    docker-compose up autotests
    
    # Run linter
    docker-compose run --rm runserver flake8

___
