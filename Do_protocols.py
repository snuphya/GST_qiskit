from utils.utils import get_circs_from_exp_design, get_exp_design, save_dataset, clear_and_mk_files
from utils.parse import Parse
from qiskit import IBMQ
import numpy as np
from qiskit import *
from qiskit.providers.ibmq.managed import IBMQJobManager
from qiskit.tools.monitor import job_monitor
from tqdm import tqdm

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q-skku', group='snu', project='snu-students')
backend = provider.get_backend('ibmq_5_yorktown')

GST_type = "smq2Q_XYICPHASE"
n_qubit = 2
num_shots_per_point = 2
max_max_length = 4
meas_key = {'00', '01', '10', '11'}

clear_and_mk_files(GST_type, max_max_length)

exp_design = get_exp_design(max_max_length, GST_type)
circs = get_circs_from_exp_design(exp_design, n_qubit)

