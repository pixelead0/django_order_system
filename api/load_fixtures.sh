#!/bin/sh
FILE="/its-migrated.txt"
if ! [ -f "$FILE" ]; then
    echo "-----------------------------------"
    echo "-- INSTALACIÓN DE FIXTURES -INI- --"
    echo "-----------------------------------"

    cd /api

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -users.user-
    python manage.py loaddata app/users/fixtures/user.json

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.customer_type-
    python manage.py loaddata customer_type --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.customer-
    python manage.py loaddata customer --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.supplier-
    python manage.py loaddata supplier --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.article-
    python manage.py loaddata article --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.delivery_associate_company-
    python manage.py loaddata delivery_associate_company --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.delivery_branch_office-
    python manage.py loaddata delivery_branch_office --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.delivery_distribution_center-
    python manage.py loaddata delivery_distribution_center --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.order-
    python manage.py loaddata order --app main

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -main.order_detail-
    python manage.py loaddata order_detail --app main

    touch $FILE
    echo "-----------------------------------"
    echo "-- INSTALACIÓN DE FIXTURES -FIN- --"
    echo "-----------------------------------"
else
    echo "--------------------------------------------"
    echo "-- Se han creado previamente los fixtures --"
    echo "--------------------------------------------"
fi

echo "-----------------------------------"
echo "-- Front   : http://0.0.0.0 "
echo "-- Back   : http://0.0.0.0:8000/admin "
echo "-- Usuario : mobilender"
echo "-- Password: Y2MzNjQyM2M0MTk5MzJk "
echo "-----------------------------------"
