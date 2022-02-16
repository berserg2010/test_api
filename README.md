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

Enter in admin panel

    username: admin
    password: password

___

### Docker
    
    # Build app
    docker-compose build backend

    # Run app
    docker-compose up --build

    # Run linter
    docker-compose run --rm backend flake8

    # Run tests
    docker-compose run --rm backend pytest

___
