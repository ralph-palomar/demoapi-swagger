import config


def create_resource(payload):
    pass


def validate_api_key(api_key, required_scopes):
    if api_key == 'testme':
        config.logger.info("Authentication successful")
        return {}
    else:
        config.logger.error("Authentication failed")
        return None


def retrieve_all_resources():
    return {}


def retrieve_resource_by_id(id):
    pass


def update_resource_by_id(id):
    pass


def delete_resource_by_id(id):
    pass
