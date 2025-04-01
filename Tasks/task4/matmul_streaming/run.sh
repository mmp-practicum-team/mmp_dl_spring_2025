# Task dimension
N=${1}
M=${2}
K=${3}
# Number of mappers
N_M=${4}
# Number of reducers
N_R=${5}

# Generate data for matrix multiplication task
python3 generate_task.py -n ${N} -m ${M} -k ${K}

# Copy all data and code to namenode (see also `docker cp`)
# Run Hadoop Streaming on namenode (see also `docker exec`)
# Copy results from namenode (see also `docker cp`)
# YOUR CODE HERE

# Check solution
python3 check_answer.py -n ${N} -m ${M} -k ${K}
