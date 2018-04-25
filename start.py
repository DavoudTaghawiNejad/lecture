from undergrad import Undergrad
from abce import Simulation, gui

simulation_parameters = {'num_undergrads': 50,
                         'lot': 2.0,
                         'initial_cost': 1.0}

# @gui(simulation_parameters)
def main(simulation_parameters):
    simulation = Simulation(processes=1)

    undergrads = simulation.build_agents(Undergrad, 'undergrad',
               number=simulation_parameters['num_undergrads'],
               **simulation_parameters)

    for r in range(250):
        simulation.advance_round(r)
        undergrads.offer_teddy()
        undergrads.buy_teddy()
        undergrads.adjust_price()
        undergrads.panel_log(goods=['money'],
                         variables=['price'])
    simulation.graphs()

if __name__ == '__main__':
    main(simulation_parameters)

