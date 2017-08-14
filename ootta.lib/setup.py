import os
import sys
from setuptools import setup, find_packages

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here,
                                                 'src',
                                                 'oottadao',
                                                 'lib')))
import releaseinfo
version = releaseinfo.__version__

setup(name='oottadao.lib',
      version=version,
      description="oottaDAO Standard Library",
      long_description="""\
Component, Driver, Variable and other plugins for oottaDAO
""",
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
      ],
      keywords='optimization multidisciplinary multi-disciplinary analysis',
      author='',
      author_email='',
      url='http://oottadao.org',
      license='Apache License, Version 2.0',
      namespace_packages=['oottadao'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={'oottadao.lib': ['casehandlers/test/*.bson',
                                     'casehandlers/test/*.json',
                                     'casehandlers/test/*.csv',
                                     'components/test/*.inp',
                                     'datatypes/domain/test/grid.in',
                                     'datatypes/domain/test/q.save',
                                     'datatypes/domain/test/lpc-test.*']},
      include_package_data=True,
      test_suite='nose.collector',
      zip_safe=False,
      install_requires=[
          'setuptools',
          'oottadao.main',
          'Pyevolve==0.6',
          'pytz>=2014.4',
          'bson==0.3.3',
          'conmin==1.0.2',
          'newsumt==1.1.1',
          'cobyla==1.0.2',
          'slsqp==1.0.2',
          'numpy',
          'scipy>=0.11.0',
          ],
      entry_points="""
      [oottadao.driver]
      oottadao.lib.drivers.adaptivesampledriver.AdaptiveSampleDriver = oottadao.lib.drivers.adaptivesampledriver:AdaptiveSampleDriver
      oottadao.lib.drivers.broydensolver.BroydenSolver = oottadao.lib.drivers.broydensolver:BroydenSolver
      oottadao.lib.drivers.caseiterdriver.CaseIteratorDriver = oottadao.lib.drivers.caseiterdriver:CaseIteratorDriver
      oottadao.lib.drivers.conmindriver.CONMINdriver = oottadao.lib.drivers.conmindriver:CONMINdriver
      oottadao.lib.drivers.cobyladriver.COBYLAdriver = oottadao.lib.drivers.cobyladriver:COBYLAdriver
      oottadao.lib.drivers.doedriver.DOEdriver = oottadao.lib.drivers.doedriver:DOEdriver
      oottadao.lib.drivers.doedriver.NeighborhoodDOEdriver = oottadao.lib.drivers.doedriver:NeighborhoodDOEdriver
      oottadao.lib.drivers.genetic.Genetic = oottadao.lib.drivers.genetic:Genetic
      oottadao.lib.drivers.iterate.FixedPointIterator = oottadao.lib.drivers.iterate:FixedPointIterator
      oottadao.lib.drivers.iterate.IterateUntil = oottadao.lib.drivers.iterate:IterateUntil
      oottadao.lib.drivers.sensitivity.SensitivityDriver = oottadao.lib.drivers.sensitivity:SensitivityDriver
      oottadao.lib.drivers.brent.Brent = oottadao.lib.drivers.brent:Brent
      [oottadao.component]
      oottadao.lib.components.expected_improvement.ExpectedImprovement = oottadao.lib.components.expected_improvement:ExpectedImprovement
      oottadao.lib.components.expected_improvement_multiobj.MultiObjExpectedImprovement = oottadao.lib.components.expected_improvement_multiobj:MultiObjExpectedImprovement
      oottadao.lib.components.external_code.ExternalCode = oottadao.lib.components.external_code:ExternalCode
      oottadao.lib.components.metamodel.MetaModel = oottadao.lib.components.metamodel:MetaModel
      oottadao.lib.components.mux.Mux = oottadao.lib.components.mux:Mux
      oottadao.lib.components.mux.DeMux = oottadao.lib.components.mux:DeMux
      oottadao.lib.components.broadcaster.Broadcaster = oottadao.lib.components.broadcaster:Broadcaster
      oottadao.lib.components.pareto_filter.ParetoFilter = oottadao.lib.components.pareto_filter:ParetoFilter
      oottadao.lib.components.linear_distribution.LinearDistribution = oottadao.lib.components.linear_distribution:LinearDistribution
      oottadao.lib.components.sleep_comp.SleepComponent = oottadao.lib.components.sleep_comp:SleepComponent
      oottadao.lib.components.linear_system.LinearSystem = oottadao.lib.componnets.linear_system:LinearSystem
      oottadao.lib.geometry.stl_group.STLGroup = oottadao.lib.components.stl_group:STLGroup
      oottadao.lib.geometry.box.BoxParametricGeometry = oottadao.lib.components.box:BoxParametricGeometry
      oottadao.lib.components.multi_metamodel.MultiFiMetaModel = oottadao.lib.components.multi_metamodel:MultiFiMetaModel
      [oottadao.surrogatemodel]
      oottadao.lib.surrogatemodels.kriging_surrogate.KrigingSurrogate = oottadao.lib.surrogatemodels.kriging_surrogate:KrigingSurrogate
      oottadao.lib.surrogatemodels.kriging_surrogate.FloatKrigingSurrogate = oottadao.lib.surrogatemodels.kriging_surrogate:FloatKrigingSurrogate
      oottadao.lib.surrogatemodels.multifi_cokriging_surrogate.MultiFiCoKrigingSurrogate = oottadao.lib.surrogatemodels.multifi_cokriging_surrogate:MultiFiCoKrigingSurrogate
      oottadao.lib.surrogatemodels.multifi_cokriging_surrogate.FloatMultiFiCoKrigingSurrogate = oottadao.lib.surrogatemodels.multifi_cokriging_surrogate:FloatMultiFiCoKrigingSurrogate
      oottadao.lib.surrogatemodels.logistic_regression.LogisticRegression = oottadao.lib.surrogatemodels.logistic_regression:LogisticRegression
      oottadao.lib.surrogatemodels.response_surface.ResponseSurface = oottadao.lib.surrogatemodels.response_surface:ResponseSurface
      [oottadao.optproblem]
      oottadao.lib.optproblems.sellar.SellarProblem = oottadao.lib.optproblems.sellar:SellarProblem
      oottadao.lib.optproblems.branin.BraninProblem = oottadao.lib.optproblems.branin:BraninProblem
      oottadao.lib.optproblems.polyscale.PolyScalableProblem = oottadao.lib.optproblems.polyscale:PolyScalableProblem
      [oottadao.caserecorder]
      oottadao.lib.casehandlers.dumpcase.DumpCaseRecorder = oottadao.lib.casehandlers.dumpcase:DumpCaseRecorder
      oottadao.lib.casehandlers.listcase.ListCaseRecorder = oottadao.lib.casehandlers.listcase:ListCaseRecorder
      oottadao.lib.casehandlers.dbcase.DBCaseRecorder = oottadao.lib.casehandlers.dbcase:DBCaseRecorder
      oottadao.lib.casehandlers.csvcase.CSVCaseRecorder = oottadao.lib.casehandlers.csvcase:CSVCaseRecorder
      oottadao.lib.casehandlers.caseset.CaseArray = oottadao.lib.casehandlers.caseset:CaseArray
      oottadao.lib.architectures.bliss.BLISS = oottadao.lib.architectures.bliss:BLISS
      oottadao.lib.casehandlers.caseset.CaseSet = oottadao.lib.casehandlers.caseset:CaseSet
      oottadao.lib.casehandlers.jsoncase.JSONCaseRecorder = oottadao.lib.casehandlers.jsoncase:JSONCaseRecorder
      oottadao.lib.casehandlers.jsoncase.BSONCaseRecorder = oottadao.lib.casehandlers.jsoncase:BSONCaseRecorder
      [oottadao.caseiterator]
      oottadao.lib.casehandlers.listcase.ListCaseIterator = oottadao.lib.casehandlers.listcase:ListCaseIterator
      oottadao.lib.casehandlers.dbcase.DBCaseIterator = oottadao.lib.casehandlers.dbcase:DBCaseIterator
      oottadao.lib.casehandlers.csvcase.CSVCaseIterator = oottadao.lib.casehandlers.csvcase:CSVCaseIterator
      oottadao.lib.casehandlers.caseset.CaseArray = oottadao.lib.casehandlers.caseset:CaseArray
      oottadao.lib.casehandlers.caseset.CaseSet = oottadao.lib.casehandlers.caseset:CaseSet
      [oottadao.casefilter]
      oottadao.lib.casehandlers.filters.ExprCaseFilter = oottadao.lib.casehandlers.filters:ExprCaseFilter
      oottadao.lib.casehandlers.filters.IteratorCaseFilter = oottadao.lib.casehandlers.filters:IteratorCaseFilter
      oottadao.lib.casehandlers.filters.SequenceCaseFilter = oottadao.lib.casehandlers.filters:SequenceCaseFilter
      oottadao.lib.casehandlers.filters.SliceCaseFilter = oottadao.lib.casehandlers.filters:SliceCaseFilter
      [oottadao.doegenerator]
      oottadao.lib.doegenerators.full_factorial.FullFactorial = oottadao.lib.doegenerators.full_factorial:FullFactorial
      oottadao.lib.doegenerators.central_composite.CentralComposite = oottadao.lib.doegenerators.central_composite:CentralComposite
      oottadao.lib.doegenerators.optlh.OptLatinHypercube = oottadao.lib.doegenerators.optlh:OptLatinHypercube
      oottadao.lib.doegenerators.uniform.Uniform = oottadao.lib.doegenerators.uniform:Uniform
      oottadao.lib.doegenerators.csvfile.CSVFile = oottadao.lib.doegenerators.csvfile:CSVFile
      [oottadao.architecture]
      oottadao.lib.architectures.bliss.BLISS = oottadao.lib.architectures.bliss:BLISS
      oottadao.lib.architectures.co.CO = oottadao.lib.architectures.co:CO
      oottadao.lib.architectures.ego.EGO = oottadao.lib.architectures.ego:EGO
      oottadao.lib.architectures.mdf.MDF = oottadao.lib.architectures.mdf:MDF
      [oottadao.parametric_geometry]
      oottadao.lib.geometry.box.BoxParametricGeometry = oottadao.lib.geometry.box:BoxParametricGeometry
      [oottadao.binpub]
      oottadao.lib.geometry.stl.STLSender = oottadao.lib.geometry.stl:STLSender
      oottadao.lib.geometry.box.BoxSender = oottadao.lib.geometry.box:BoxSender
      oottadao.lib.geometry.stl_group.STLGroupSender = oottadao.lib.geometry.stl_group:STLGroupSender
      """,
      )
