#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd


class Plotting(object):
	def __init__(self):
		self.data_dir = 'data/'
		self.fig_dir = 'figures/'

	def plot_rates_full_simulation(self):
		'''
		Plots the neuron rates for the full 4s simulation
		:return: None
		'''

		rates_data = pd.DataFrame.from_csv(self.data_dir + 'standard_sim_neuron_rates_4000.csv')
		flipped_data = rates_data.reindex(index=rates_data.index[::-1]) # flipping the neuron indices to match the
		# plotting style of Haga and Fukai

		plt.pcolor(flipped_data, cmap='hot_r')
		plt.yticks([0, 100, 200, 300, 400, 500], [500, 400, 300, 200, 100, 0])
		plt.xticks(np.arange(0, len(rates_data.columns) + len(rates_data.columns) / 8, len(rates_data.columns) / 8),
				   [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
		plt.ylabel('Neuron #', fontsize=10)
		plt.xlabel('Time (s)', fontsize=10)
		cbar = plt.colorbar()
		cbar.ax.set_title('Rate (Hz)', fontsize=10)
		plt.savefig(self.fig_dir + 'full_simulation_rates')
		plt.show()

	def plot_middle_weight_3s_simulation(self):
		'''
		Plots the weights between the middle neuron and the rest of the neurons at the 3s mark
		:return: None
		'''

		weights_data = pd.DataFrame.from_csv(self.data_dir + 'standard_sim_neuron_weights_3000.csv')
		weight_array = weights_data.values
		weight_initial_data = pd.DataFrame.from_csv(self.data_dir + 'weights_initial.csv')
		weight_initial = weight_initial_data.values

		middle_weight_diff = weight_array[:,249] - weight_initial[:,249]

		plt.figure(figsize=(5, 1.5))
		plt.gcf().subplots_adjust(bottom=0.4, left=0.1, right=0.95)
		plt.plot(np.arange(200, 301), middle_weight_diff[200:301])
		plt.xlim(200, 300)
		plt.ylim(0, 3)
		plt.plot(np.arange(200,301), middle_weight_diff[200:301], 'b')
		plt.xlabel('Neuron #')
		plt.ylabel('Change')
		plt.savefig(self.fig_dir + 'weights_3s')
		plt.show()

	def plot_rates_additional_one_sec_simulation(self):
		'''
		Plots the neuron rates for the additional one second in an attempt for a forward replay
		:return: None
		'''

		rates_data = pd.DataFrame.from_csv(self.data_dir + 'additional_one_sec_neuron_rates_1000.csv')
		flipped_data = rates_data.reindex(index=rates_data.index[::-1]) # flipping the neuron indices to match the
		# plotting style of Haga and Fukai

		plt.pcolor(flipped_data, cmap='hot_r')
		plt.yticks([0, 100, 200, 300, 400, 500], [500, 400, 300, 200, 100, 0])
		#plt.xticks(np.arange(0, len(rates_data.columns) + len(rates_data.columns) / 8, len(rates_data.columns) / 8),
		#		   [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
		plt.ylabel('Neuron #', fontsize=10)
		plt.xlabel('Time (s)', fontsize=10)
		cbar = plt.colorbar()
		cbar.ax.set_title('Rate (Hz)', fontsize=10)
		plt.savefig(self.fig_dir + 'additional_one_sec_simulation_rates')
		plt.show()

	def plot_middle_weight_additional_one_sec_simulation(self):
		'''
		Plots the weights between the middle neuron and the rest of the neurons at the 5s mark
		:return: None
		'''

		weights_data = pd.DataFrame.from_csv(self.data_dir + 'additional_one_sec_neuron_weights_1000.csv')
		weight_array = weights_data.values
		weight_initial_data = pd.DataFrame.from_csv(self.data_dir + 'weights_initial.csv')
		weight_initial = weight_initial_data.values

		middle_weight_diff = weight_array[:,249] - weight_initial[:,249]

		plt.figure(figsize=(10, 2))
		plt.gcf().subplots_adjust(bottom=0.25, left=0.1, right=0.95)
		plt.plot(np.arange(200,301), middle_weight_diff[200:301], 'b')
		plt.xlim(200, 300)
		plt.ylim(0, 10)
		plt.xlabel('Neuron #')
		plt.ylabel('Change')
		plt.savefig(self.fig_dir + 'weights_additional_one_sec')
		plt.show()

	def plot_rates_additional_four_sec_simulation(self):
		'''
		Plots the neuron rates for the additional 4s simulation
		:return: None
		'''

		rates_data = pd.DataFrame.from_csv('data/additional_four_sec_neuron_rates.csv')
		flipped_data = rates_data.reindex(index=rates_data.index[::-1]) # flipping the neuron indices to match the
		# plotting style of Haga and Fukai

		plt.pcolor(flipped_data, norm=colors.LogNorm(vmin=1, vmax=flipped_data.values.max()),
				   cmap='hot_r')
		plt.yticks([0, 100, 200, 300, 400, 500], [500, 400, 300, 200, 100, 0])
		plt.xticks(np.arange(0, len(rates_data.columns) + len(rates_data.columns) / 8, len(rates_data.columns) / 8),
				   [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
		plt.ylabel('Neuron #', fontsize=10)
		plt.xlabel('Time (s)', fontsize=10)
		cbar = plt.colorbar()
		cbar.ax.set_title('Rate (Hz)', fontsize=10)
		plt.savefig(self.fig_dir + 'additional_four_sec_simulation_rates')
		plt.show()

	def plot_middle_weight_4s_simulation(self):
		'''
		Plots the weights between the middle neuron at the rest of the neurons at the 4s mark
		:return: None
		'''

		weights_data = pd.DataFrame.from_csv(self.data_dir + 'neuron_weights_4000.csv')
		weight_array = weights_data.values
		weight_initial_data = pd.DataFrame.from_csv(self.data_dir + 'weights_initial.csv')
		weight_initial = weight_initial_data.values

		middle_weight_diff = weight_array[:,249] - weight_initial[:,249]

		plt.figure(figsize=(10, 2))
		plt.plot(np.arange(200,301), middle_weight_diff[200:301])
		plt.xlabel('Neuron #')
		plt.ylabel('Change')

		plt.show()

	def plot_custom_simulation(self):
		'''
		Change the parameters as required.
		:return: None
		'''

		rates_data = pd.DataFrame.from_csv('data/additional_eight_sec_neuron_rates.csv')
		flipped_data = rates_data.reindex(index=rates_data.index[::-1])  # flipping the neuron indices to match the
		# plotting style of Haga and Fukai

		plt.pcolor(flipped_data, norm=colors.LogNorm(vmin=1, vmax=flipped_data.values.max()),
				   cmap='hot_r')
		plt.yticks([0, 100, 200, 300, 400, 500], [500, 400, 300, 200, 100, 0])
		plt.xticks(np.arange(0, len(rates_data.columns) + len(rates_data.columns) / 8, len(rates_data.columns) / 8),
				   [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
		plt.ylabel('Neuron #', fontsize=10)
		plt.xlabel('Time (s)', fontsize=10)
		cbar = plt.colorbar()
		cbar.ax.set_title('Rate (Hz)', fontsize=10)
		plt.savefig(self.fig_dir + 'additional_eight_sec_simulation_rates')
		plt.show()

if __name__ == "__main__":
	plots = Plotting()
	plots.plot_custom_simulation()
	# plots.plot_rates_full_simulation()
	# plots.plot_middle_weight_3s_simulation()
	# plots.plot_middle_weight_4s_simulation()
	# plots.plot_rates_additional_one_sec_simulation()
	# plots.plot_rates_additional_four_sec_simulation()
	# plots.plot_middle_weight_additional_one_sec_simulation()