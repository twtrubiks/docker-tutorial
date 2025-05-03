#!/bin/bash

# 要更新的 db
DATABASES=("odoo1" "odoo2" "odoo3")

for DB in "${DATABASES[@]}"
do
    echo "Updating addons for database: $DB"

    # 設定環境變數 DB_NAME 並執行 docker compose
    DB_NAME=$DB docker compose up -d

    # 等待 Odoo 完成資料庫更新
    sleep 10  # 視需求調整等待時間
done

echo "All databases have been updated."