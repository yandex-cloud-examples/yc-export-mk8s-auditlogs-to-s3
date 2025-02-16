# Экспорт аудитных логов Kubernetes в Object Storage

В данном сценарии Terraform показано развертывание функции Cloud Functions c помощью триггера, извлечение аудитных логов кластера Kubernetes из группы Cloud Logging, а также сохранение таких логов в бакет Object Storage. 

Группа Cloud Logging может быть настроена для работы с Yandex Data Streams для одновременной передачи аудитых логов в YDS.
Подробнее см. в инструкции [Создание лог-группы с помощью CLI](https://yandex.cloud/en/docs/logging/operations/create-group).

![image](https://user-images.githubusercontent.com/85429798/186873514-06d204c4-06e8-4239-93be-39817a197f4b.png)

Предварительные условия:

- ✅ Кластер Managed K8s.
- ✅ Лог-группа Cloud Logging.
- ✅ Terraform.

1. Для работы с модулем из России создайте файл `~/.terraformrc` и укажите в нем параметры сетевого зеркала Yandex Cloud:
    ```
    cat ~/.terraformrc
    provider_installation {
      network_mirror {
        url = "https://terraform-network-mirror.storage.yandexcloud.net/"
      }
    }
    ```
1. Заполните поля в файле `provider.tf`: укажите токен для аутентификации или используйте файл с ключом сервисного аккаунта.
1. Создайте файл `private.auto.tfvars` и заполните в нем все необходимые переменные (пример файла `private.auto.tfvars` приведен ниже).
1. Выполните следующие команды:

    ```
    terraform init
    terraform apply
    ```

Пример файла `private.auto.tfvars`:

```
cloud_id  = "b1g3xxxxxxxxxxxxxxxx"
folder_id = "b1g7xxxxxxxxxxxxxxxx"
cluster_id = "catsxxxxxxxxxxxxxxxx"
logging_group_id = "e23oxxxxxxxxxxxxxxxx"
storage_bucket_name = "audit-log-bucket-xxxxxx"
```
