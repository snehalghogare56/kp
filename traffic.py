66)  Build an expert system for traffic control signal
class TrafficControlExpertSystem:
    def __init__(self):
        self.rules = [
            {'condition': 'heavy_traffic', 'signal': 'red'},
            {'condition': 'moderate_traffic', 'signal': 'yellow'},
            {'condition': 'light_traffic', 'signal': 'green'}
        ]

    def get_traffic_signal(self, traffic_condition):
        for rule in self.rules:
            if rule['condition'] == traffic_condition:
                return rule['signal']
        return 'unknown'

if __name__ == "__main__":
    expert_system = TrafficControlExpertSystem()

    # Example usage
    traffic_condition = input("Enter traffic condition (heavy_traffic, moderate_traffic, light_traffic): ")
    signal = expert_system.get_traffic_signal(traffic_condition)

    if signal != 'unknown':
        print(f"The recommended traffic signal is {signal}.")
    else:
        print("Unknown traffic condition.")
