import argparse

class EnterpriseTCOEngine:
    """
    Advanced economic modeling for AI Infrastructure.
    Used by AI Executive Advisors to build business cases for GPU clusters.
    """
    def __init__(self, node_count: int, gpu_per_node: int = 8):
        self.node_count = node_count
        self.total_gpus = node_count * gpu_per_node
        # Baseline costs for NVIDIA H100 systems
        self.node_cost = 350000 
        self.networking_overhead = 0.20 # 20% for Cisco fabric

    def calculate_3yr_tco(self, power_kwh_rate: float, watt_per_node: int = 10000):
        capex = (self.node_cost * self.node_count) * (1 + self.networking_overhead)
        
        # Power costs
        daily_kwh = (watt_per_node * 24 * self.node_count) / 1000
        annual_power_cost = daily_kwh * 365 * power_kwh_rate
        
        # OpEx (Cooling, Maintenance, Software)
        annual_opex = annual_power_cost + (capex * 0.10)
        
        total_tco = capex + (annual_opex * 3)
        return {
            "CapEx_Investment": capex,
            "Annual_OpEx": annual_opex,
            "Total_3Yr_TCO": total_tco,
            "Cost_Per_GPU_Hour": total_tco / (3 * 365 * 24 * self.total_gpus)
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strategic AI TCO Engine")
    parser.add_argument("--nodes", type=int, required=True)
    parser.add_argument("--power_cost", type=float, default=0.12)
    args = parser.parse_args()

    engine = EnterpriseTCOEngine(args.nodes)
    report = engine.calculate_3yr_tco(args.power_cost)

    print("==========================================")
    print("STRATEGIC AI INFRASTRUCTURE ECONOMIC REPORT")
    print("==========================================")
    for k, v in report.items():
        print(f"{k:20}: ${v:,.2f}")
