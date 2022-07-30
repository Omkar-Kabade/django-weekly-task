from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

weekDays = {
    "monday": "Wake Up And Do Yoga",
    "tuesday": "Wake Up And Do Meditation",
    "wednesday": "Wake Up And Do Go For Jogging",
    "thursday": "Wake Up And Do Exercise",
    "friday": "Wake Up And Read Books",
    "saturday": "It's Saturday Have Some Rest!",
    "sunday": "Sunday It Is Netflix And Chill!"
}


def index(request):
    days = list(weekDays.keys())
    dayList = ""
    try:
        return render(request , "tasks/index.html",{
            "days":days
        })
    except:
        return render(request , "tasks/index.html",{})


def weekDayByNumber(request, day):
    allDays = list(weekDays.keys())
    if day>len(allDays):
        return HttpResponseNotFound ("no task has been added for this day yet!")
    actual_day = allDays[day-1]
    redirect_path = reverse("week-day",args = [actual_day])
    return HttpResponseRedirect(redirect_path)


def weekDay(request, day):
    try:
        actual_task = weekDays[day]
        return render (request , "tasks/task.html" ,{
            "task":actual_task,
            "day":day
        })
    except:
        return HttpResponseNotFound("something went wrong!")


