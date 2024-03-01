# your_app/tasks.py
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def log_create_action(instance_id):
    try:
        logger.info('Task log_create_action started for instance_id: {}'.format(instance_id))
        # Your existing task logic here
        result = "Se agrego el usuario con exito"
        logger.info('Task log_create_action completed successfully')
        return result
    except Exception as e:
        logger.error('Task log_create_action failed: {}'.format(str(e)))
        raise


@shared_task
def log_update_action(instance_id):
    return "Se edito el usuario con exito"

@shared_task
def log_delete_action(instance_id):
    return "Se elimino el usuario con exito"


@shared_task
def add(x, y):
    return x+y