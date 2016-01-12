# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from stl.mesh import Mesh


class AppScene(object):
	'''
	Class holding data of scene, models, positions, parameters
	it can be used for generating sliced data and rendering data
	'''
	def __init__(self):
		self.model = []






class Model(object):
	'''
	this is reprezentation of model data, data readed from file
	'''
	def __init__(self):
		self.v0 = []
		self.v1 = []
		self.v2 = []


class ModelTypeAbstract(object):
	'''
	model type is abstract class, reprezenting reading of specific model data file
	'''
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	@abstractmethod
	def load(filename):
		print "This is abstract model type"
		return None



class ModelTypeStl(ModelTypeAbstract):
	'''
	Concrete ModelType class for STL type file, it can load binary and char file
	'''
	
	def load(self, filename):
		print "this is STL file reader"
		mesh = Mesh.from_file(filename)
		model = Model()

		for i in xrange(len(mesh.v0)):
			model.v0.append(mesh.v0[i])
			model.v1.append(mesh.v1[i])
			model.v2.append(mesh.v2[i])
		'''
		some magic with model data
		'''
		return model


