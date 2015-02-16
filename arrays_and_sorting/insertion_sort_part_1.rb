def insertionSort(ar) 
  i, j = ar[-1], ar.length-2

  while j >= -1
    if ar[j] > i && (j > 0)
     ar[j+1] = ar[j]
     puts ar.join(' ')            
    elsif ar[j] <= i
      ar[j+1] = i
      puts ar.join(' ')
      break
    end
    j -= 1
  end
end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}

insertionSort(ar)