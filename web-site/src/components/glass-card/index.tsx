import { ReactElement } from 'react';
import './index.scss';

interface IProps {
  children?: ReactElement;
  className?: string;
}

const GlassCard = (props: IProps) => {
  const { className = '', children } = props;
  return <div className={`glass-card ${className}`}>{children}</div>;
};

export default GlassCard;
