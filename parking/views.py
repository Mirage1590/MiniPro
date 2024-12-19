from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ParkingSpot, Reservation
from django.utils import timezone

# View สำหรับหน้าแรก (แสดงรายการที่จอดรถ)
def home(request):
    parking_spots = ParkingSpot.objects.all()
    return render(request, 'home.html', {'parking_spots': parking_spots})

# View สำหรับการจองที่จอดรถ
def reserve_parking(request, spot_id):
    parking_spot = ParkingSpot.objects.get(id=spot_id)

    if request.method == 'POST':
        # รับข้อมูลจากแบบฟอร์มการจอง
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        # สร้าง Reservation ใหม่
        reservation = Reservation.objects.create(
            user=request.user,
            parking_spot=parking_spot,
            start_time=start_time,
            end_time=end_time
        )

        # อัปเดตสถานะของที่จอดรถเป็น "Occupied" หลังจากการจอง
        parking_spot.status = 'Occupied'
        parking_spot.save()

        # เมื่อจองเสร็จแล้ว, ให้กลับไปที่หน้าแรก
        return redirect('home')

    return render(request, 'reserve_parking.html', {'parking_spot': parking_spot})
