# Threshold-Examples
OpenCV + Python

<h2>Binary Thresholding ( type = THRESH_BINARY )</h2>
<pre>
if src(x,y) > thresh
    dst(x,y) = maxValue
else
    dst(x,y) = 0
</pre>

<h2>Inverse Binary Thresholding ( type = THRESH_BINARY_INV )</h2>
<pre>
if src(x,y) > thresh
  dst(x,y) = 0
else
  dst(x,y) = maxValue
</pre>

<h2>Truncate Thresholding ( type = THRESH_TRUNC )</h2>
<pre>
if src(x,y) > thresh
  dst(x,y) = thresh
else
  dst(x,y) = src(x,y)
</pre>

<h2>Threshold to Zero ( type = THRESH_TOZERO )</h2>
<pre>
if src(x,y) > thresh
  dst(x,y) = src(x,y)
else
  dst(x,y) = 0
</pre>
<h2>Inverted Threshold to Zero ( type = THRESH_TOZERO_INV)</h2>
<pre>
if src(x,y) > thresh
  dst(x,y) = 0
else
  dst(x,y) = src(x,y)
</pre>
