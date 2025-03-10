# os-semaphore

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name semaphore_lab python=3.13.1</li>
		<li>conda activate semaphore_lab</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the semaphore_lab anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
   <li><b>Buffer class</li></b></li>
    <ol>
      <li>The buffer class will represent the bounded buffer</li>
      <li>__init__ should take in size as a parameter</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>size: size of the buffer</li>
          <li>items: list to store items in the buffer.</li>
          <li>in_pointer: initialize to 0</li>
          <li>out_pointer: initialize to 0</li>
		<li>mutex: a threading lock</li>
		<li>empty_slots: a threading semaphore to indicate how many slots are empty</li>
		<li>full_slots: a threading semaphore to indicate how many slots are full</li></ol>
<li><b>Producer class</b></li>
    <ol>
      <li>The producer will produce processes represented as integers to add to the buffer. This will subclass the threading Python class.</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>buffer (required)</li>
	<li>id (required): an int used to identify a producing process</li>
        </ol>
    <li><b>Methods</b></li>
      <ol>
        <li>produce(): Takes an item as a parameter and add the item to the buffer. It must acquire and relase appropriate locks. When the item is added to the buffer, print out "Produced: {item} at postition {position in the buffer}</li>
	<li>run(): Overload the built in threading run() method to generate 10 random integers between 1 and 100 and produce to the buffer. Also print out "Producer {id} producting {item}..." after generating the item to add to the buffer.</li>
      </ol>
	    
  </ol>

