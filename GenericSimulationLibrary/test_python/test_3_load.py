try:
        from GenericSimulationLibrary import SimulationInterface
except:
        from simulation_interface import SimulationInterface

SI = SimulationInterface()
SI.load("test_2.sim")
SI.export_xlsx("test_3.xlsx")
SI.plot()