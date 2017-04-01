# ----------------------------------------------------------------
# TELLURIUM API
# ----------------------------------------------------------------

# General
from .tellurium import (
    getVersionInfo,
    printVersionInfo,
    getTelluriumVersion,
    noticesOff,
    noticesOn,
    saveToFile,
    readFromFile,
    )

# Converters
from .teconverters import (
    antimonyConverter,
    inlineOmex,
    )

# Model import
from .tellurium import (
    loadAntimonyModel,     # load antimony from string
    loada,                 # same as loadAntimonyModel
    loadSBMLModel,         # load sbml from string
    loads,                 # same as loadSBMLModel
    )

# Keeps a dictionary of loaded models
from .tellurium import (
    __set_model, # associates model name with roadrunner instance
    model,       # retrieve a roadrunner instance previously set with __set_model
    )

# Legacy import, use antimonyConverter
from .tellurium import (
    antimonyToSBML,
    sbmlToAntimony,
    )

# CellML converters
if hasattr(tellurium, 'loadCellMLModel'):
    from .tellurium import (
        loadCellMLModel,
        antimonyToCellML,
        sbmlToCellML,
        cellmlToAntimony,
        cellmlToSBML,
        )

# Plotting
from .tellurium import (
    getPlottingEngine,
    getDefaultPlottingEngine,
    setDefaultPlottingEngine,
    )
# Legacy plotting
from .tellurium import (
    plotArray,
    plotWithLegend,
    )

# Test models
from .tellurium import (
    loadTestModel,
    getTestModel,
    listTestModels,
    )

# Latex
from .teio.latex import LatexExport

# Parameter scanning
from .analysis.parameterscan import (
    ParameterScan,
    SteadyStateScan,
    )

# sedml support
from .sedml.tesedml import sedmlToPython, executeSEDML

# Combine archive support
from .tellurium import (
    convertAndExecuteCombineArchive,
    exportInlineOmex,
    executeInlineOmex,
    executeInlineOmexFromFile,
)

# Do not use
# from .sedml.tephrasedml import experiment
# from .tecombine import combine

# Misc
from .tellurium import getEigenvalues

# import .optimization  # nothing here
# import .visualization # display with graphviz
# import .tests         # needs to be refactored for Python 3

try:
    import temiriam
except ImportError:
    pass

# Needs to be checked for compatibility with latest Jupyter and Python 3
# import notebooks

__version__ = getTelluriumVersion()
