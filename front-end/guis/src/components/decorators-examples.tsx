
import { React } from "react";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import { connect } from "http2";

function mapStateToProps(state) {
  return {
    todos: state.todos
  }
}

function mapDispatchToProps(dispatch) {
  return {
    action: () => dispatch()
  }
}

@connect(mapStateToProps, mapDispatchToProps)
const MyApp: React.FC = ({}) => {
  return (
    <div>

    </div>
  );
}

export default MyApp;

// export default connect(mapStateToProps, mapDispatchToProps)(MyApp);
