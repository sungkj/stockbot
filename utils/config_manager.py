import yaml
import os

class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path

    def load(self):
        if not os.path.exists(self.config_path):
            return {}
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def save(self, config_data):
        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(config_data, f, allow_unicode=True, sort_keys=False)

    def add_stock(self, stock_name):
        config = self.load()
        if 'stocks' not in config:
            config['stocks'] = {}
        if stock_name not in config['stocks']:
            config['stocks'][stock_name] = []
            self.save(config)
            return True
        return False

    def add_keyword(self, stock_name, keyword):
        config = self.load()
        if 'stocks' not in config:
            config['stocks'] = {}
        if stock_name not in config['stocks']:
            config['stocks'][stock_name] = []
        if keyword not in config['stocks'][stock_name]:
            config['stocks'][stock_name].append(keyword)
            self.save(config)
            return True
        return False

    def get_stocks(self):
        config = self.load()
        return config.get('stocks', {})
