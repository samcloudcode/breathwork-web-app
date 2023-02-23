import streamlit as st
from Breath_Classes import Action, BreathCycle, BreathSequence
import time

if 'view' not in st.session_state:
    st.session_state['view'] = 'browse'


def switch_view(target_view):
    st.session_state['view'] = target_view


def display_browse():
    st.set_page_config()
    st.title("Breath Sequences")

    list_options = ('a', 'b', 'c')

    st.selectbox(label='Select Sequence', options=list_options)
    st.markdown('This is a description of the breath sequence')

    st.button("Edit Sequence", on_click=switch_view, args=('edit_sequence',))
    st.button("Create New Sequence", on_click=switch_view, args=('edit_sequence',))

    st.slider("Max Breath Cycle", min_value=1, max_value=10, step=1)
    st.slider("Time", min_value=1, max_value=10, step=1)

    st.button("Start", on_click=switch_view, args=('play',))


def display_sequence(sequence_object):
    st.text_input('Sequence Name')
    st.text_area('Sequence Description')
    sequence_container = st.container()
    expander = st.expander('**Breath 1**', expanded=True)

    with sequence_container:
        with expander:
            options = ('Breath 1', 'Breath 2')
            col_1, col_2, col_3 = st.columns([3, 1, 1])
            with col_1:
                st.selectbox('Breath Cycle', options=options)
                st.text('Summary of Breath')
            with col_2:
                st.number_input('Scale', value=1)
                st.metric('Cycle Time', "30s")
            with col_3:
                st.number_input('Repeat', value=1)
                st.metric('Total Time', "6m30s")

            col_1, col_2, col_3 = st.columns([3, 1, 1])

            with col_1:
                st.button('Add Breath Cycle')
            with col_2:
                st.button('Edit')
            with col_3:
                st.button('Delete')

            # Consider adding move up/down

    st.button("Create New Breath Cycle", on_click=switch_view, args=('new_cycle',))

    st.button("Save and Close", on_click=switch_view, args=('browse',))


def add_breath_cycle(sequence_container):
    pass

def add_action_row():

    with st.expander('**Name**', expanded=True):
        col_1, col_2, col_3, col_4 = st.columns([2, 1, 1, 1])

        with col_1:
            st.text_input('Action')
            st.checkbox('Scalable')
        with col_2:
            st.number_input('Start Capacity(%)', value=20, step=5, max_value=100, min_value=0)
        with col_3:
            st.number_input('End Capacity(%)', value=80, step=5)
            st.button('Delete')
        with col_4:
            st.number_input('Time(s)', value=1)
            st.button('Duplicate')

def display_cycle(cycle_object):
    st.text_input('Cycle Name')
    st.text_area('Cycle Description')
    st.markdown("Actions")

    add_action_row()
    if st.button("Add new Action"):
        add_action_row()

    st.button("Save and Close", on_click=switch_view, args=('edit_sequence', ))


def display_action(action_object):
    st.button("Close", on_click=switch_view, args=('edit_cycle',))


def display_play():
    st.set_page_config()
    st.title("Action")
    st.title("5")

    st.button("Stop", on_click=switch_view, args=('browse',))


match st.session_state['view']:
    case 'browse':
        display_browse()

    case 'play':
        display_play()

    case 'edit_sequence':
        st.title("Edit Sequence")
        sequence = BreathSequence()
        display_sequence(sequence)

    case 'new_sequence':
        st.title("Create New Sequence")
        sequence = BreathSequence()
        display_sequence(sequence)

    case 'new_cycle':
        st.title("Create New Breath Cycle")
        cycle = BreathCycle()
        display_cycle(cycle)

    case 'edit_cycle':
        st.title("Edit Breath Cycle")
        cycle = BreathCycle()
        display_cycle(cycle)

    case 'edit_action':
        st.title("Edit Action")
        action = Action()
        display_action(action)

    case 'new_action':
        st.title("Create New Action")
        action = Action()
        display_action(action)
