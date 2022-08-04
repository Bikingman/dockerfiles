docker run  --rm \
     -d \
     -e PASSWORD=password \
     -v $(pwd)/src:/src \
     -p 8787:8787 \
     rstudio