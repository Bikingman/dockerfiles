docker build -t nhts .
docker run -v $(pwd):/src -i -t -p 8889:8889 nhts
conda activate nhts
cd ..
cd src
