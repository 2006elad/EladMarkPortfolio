import time
import check_limit_functions as lim_ck
import db_data_functions as db_fun
from pyfirmata import Arduino, util


board = Arduino('COM3')
it = util.Iterator(board)
it.start()
pin9 = board.get_pin('d:9:s')
board.pass_time(2)


def servo_open():
    pin9.write(20)


def servo_close():
    pin9.write(0)


def open_box():
    if lim_ck.i_did_not_exceed_my_day_limit() and lim_ck.i_did_not_exceed_my_hour_limit() and \
            lim_ck.this_is_not_restricted_hours():
        servo_open()
        db_fun.add_timestamp()
        time.sleep(15)
        servo_close()


def read_box_state():
    board.analog[0].enable_reporting()
    print("waiting for box state change")

    is_open_already = False
    while True and not is_open_already:
        one_listen = board.analog[0].read()
        if one_listen is not None:
            one_listen = int(one_listen)
            if one_listen == 1:
                print("box is open")
                open_box()
                is_open_already = True
        time.sleep(0.1)
