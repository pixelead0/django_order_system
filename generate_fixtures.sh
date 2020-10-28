# This script create a new fixtures for django

echo [$(date +"%Y-%m-%d %T")] --Started--

mkdir -p api/app/users/fixtures/

# Auth
echo [$(date +"%Y-%m-%d %T")] creating fixtures from -auth.user-
docker-compose exec api python manage.py dumpdata auth.user --indent=2 >api/app/users/fixtures/user.json

mkdir -p api/app/main/fixtures/

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.customertype-
docker-compose exec api python manage.py dumpdata main.customertype --indent=2 >api/app/main/fixtures/customer_type.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.customer-
docker-compose exec api python manage.py dumpdata main.customer --indent=2 >api/app/main/fixtures/customer.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.supplier-
docker-compose exec api python manage.py dumpdata main.supplier --indent=2 >api/app/main/fixtures/supplier.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.article-
docker-compose exec api python manage.py dumpdata main.article --indent=2 >api/app/main/fixtures/article.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.deliveryassociatecompany-
docker-compose exec api python manage.py dumpdata main.deliveryassociatecompany --indent=2 >api/app/main/fixtures/delivery_associate_company.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.deliverybranchoffice-
docker-compose exec api python manage.py dumpdata main.deliverybranchoffice --indent=2 >api/app/main/fixtures/delivery_branch_office.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.deliverydistributioncenter-
docker-compose exec api python manage.py dumpdata main.deliverydistributioncenter --indent=2 >api/app/main/fixtures/delivery_distribution_center.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.order-
docker-compose exec api python manage.py dumpdata main.order --indent=2 >api/app/main/fixtures/order.json

echo [$(date +"%Y-%m-%d %T")] creating fixtures from -main.order_detail-
docker-compose exec api python manage.py dumpdata main.orderdetail --indent=2 >api/app/main/fixtures/order_detail.json

echo [$(date +"%Y-%m-%d %T")] --Finished--
