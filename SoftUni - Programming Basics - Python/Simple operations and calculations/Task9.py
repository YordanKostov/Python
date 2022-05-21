length_in_cent = int(input())
width_in_cent = int(input())
heigth_in_cent = int(input())
percentage_volume = float(input()) * 0.01

volume = length_in_cent * width_in_cent * heigth_in_cent
total_litres = volume * 0.001
litres_to_fill = total_litres * (1-percentage_volume)

print(f'{litres_to_fill:.3f}')