docker build -t postgresql_env .
docker run -v $(pwd):/src -i -t -p 8888:8888 postgresql_env
conda activate postgresql_env
cd ..
cd src
