#!/bin/bash
python -c "import neural_compressor as nc;print(nc.version.__version__)"
echo "run neural insights ut..."

# Install Neural Solution
bash /neural-compressor/.azure-pipelines/scripts/install_neural_insights.sh

# Install requirements for test
cd /neural-compressor/neural_insights/test || exit 1
if [ -f "requirements.txt" ]; then
    n=0
    until [ "$n" -ge 3 ]
    do
        python -m pip install --no-cache-dir -r requirements.txt && break
        n=$((n+1))
        sleep 5
    done
    pip list
else
    echo "Not found requirements.txt file."
fi

cd /neural-compressor/neural_insights || exit 1
find ./test -name "test*.py" | sed 's,\.\/,python ,g' | sed 's/$/ --verbose/' > run.sh

LOG_DIR=/neural-compressor/log_dir
mkdir -p ${LOG_DIR}
ut_log_name=${LOG_DIR}/ut_neural_insights.log

echo "cat run.sh..."
cat run.sh | tee ${ut_log_name}
echo "------UT start-------"
bash run.sh 2>&1 | tee -a ${ut_log_name}
echo "------UT end -------"

if [ $(grep -c "FAILED" ${ut_log_name}) != 0 ] || [ $(grep -c "core dumped" ${ut_log_name}) != 0 ] || [ $(grep -c "OK" ${ut_log_name}) == 0 ];then
    echo "Find errors in UT test, please check the output..."
    exit 1
fi
echo "UT finished successfully! "